import { getInstallationOctokit } from "./githubAuth.js";
 export async function handlePullRequest(event) {
  const action = event.action;
  const pr = event.pull_request;

  const allowedActions = ["opened", "reopened", "synchronize"];
  if (!allowedActions.includes(action)) {
    console.log(`Skipping PR action: ${action}`);
    return;
  }

  if (!pr || pr.state !== "open") {
    console.log("PR is closed, skipping");
    return;
  }

  if (!event.installation?.id) {
    console.log("No installation found, skipping");
    return;
  }
  console.log("Processing PR action:", action);

  const installationId = event.installation.id;
  const owner = pr.base.repo.owner.login;
  const repo = pr.base.repo.name;
  const prNumber = pr.number;
  const prHeadSha = pr.head.sha;

  const octokit = await getInstallationOctokit(installationId);

  //Fetch changed files in this PR
  const changedFiles = await getChangedFilesFromPR(
    octokit,
    owner,
    repo,
    prNumber
  );

  console.log("Changed files:", changedFiles.map(f => f.path));

  //Fetch full file contents for scanning
  const filesForScan = [];
  for (const file of changedFiles) {
    if (file.status !== "removed") {
      const content = await getFileContent(
        octokit,
        owner,
        repo,
        file.path,
        prHeadSha
      );
      filesForScan.push({
        path: file.path,
        content,
      });
    }
  }

  //Mock scan result
  const scanResult = {
    score: 82,
    findings: { high: 1, medium: 2, low: 3 },
    files: filesForScan.map(f => ({
      path: f.path,
      issue: "Example security issue",
    })),
  };
async function getChangedFilesFromPR(octokit, owner, repo, prNumber) {
  const files = [];
  let page = 1;

  while (true) {
    const response = await octokit.pulls.listFiles({
      owner,
      repo,
      pull_number: prNumber,
      per_page: 100,
      page,
    });

    for (const file of response.data) {
      files.push({
        path: file.filename,
        status: file.status, // added | modified | removed
        patch: file.patch,   // diff (may be undefined)
        sha: file.sha,
      });
    }

    if (response.data.length < 100) break;
    page++;
  }

  return files;
}
  //Post bot comment
  const body = buildMarkdownReport(scanResult,changedFiles, owner, repo);

  await octokit.issues.createComment({
    owner,
    repo,
    issue_number: prNumber,
    body,
  });

  console.log("Bot comment posted successfully");
}
async function getFileContent(octokit, owner, repo, path, ref) {
  try {
    const response = await octokit.repos.getContent({
      owner,
      repo,
      path,
      ref,
    });

    // GitHub returns Base64 encoded content
    if (response.data && response.data.content) {
      const decoded = Buffer.from(response.data.content, "base64").toString("utf8");
      console.log('fetched', path);
      console.log('content', decoded.slice(0,100));

      return decoded;

    }
  } catch (err) {
    console.warn(`Could not fetch content for ${path}`);
  }

  return null;
}


function buildMarkdownReport(result, changedFiles, owner, repo) {
  return `

## Pervazive AI Scan Report

**AI Score:** ${result.score} / 100

### Findings Summary
| Severity | Count |
|---------|-------|
| High | ${result.findings.high} |
| Medium | ${result.findings.medium} |
| Low | ${result.findings.low} |

### Changed Files in this PR
${changedFiles
  .map(
    f =>
      `- [\`${f.path}\`](https://github.com/${owner}/${repo}/blob/main/${f.path}) (${f.status})`
  )
  .join("\n")}
### Vulnerable Files
${result.files
  .map(
    (f) =>
      `- [\`${f.path}\`](https://github.com/${owner}/${repo}/blob/main/${f.path}) — ${f.issue}`
  )
  .join("\n")}

<details>
<summary>Why this matters</summary>

These issues may impact extension security and user data safety.
</details>
`;
}