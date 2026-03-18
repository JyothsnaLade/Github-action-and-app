def greet(name):
 """
 This function greets the person passed in as a parameter.
 """
 print(f"Hi there, {name}!")
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone() 