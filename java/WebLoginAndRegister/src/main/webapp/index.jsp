<!DOCTYPE html>
<html>
<head>
    <title>Login and Registration</title>
</head>
<body>
    <h2>Register</h2>
    <form action="UserServlet" method="post">
        <input type="hidden" name="action" value="register">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        <input type="submit" value="Register">
    </form>

    <h2>Login</h2>
    <form action="UserServlet" method="post">
        <input type="hidden" name="action" value="login">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
