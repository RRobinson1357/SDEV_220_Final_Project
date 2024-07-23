<!DOCTYPE html>
<html lang='en'>
<title>Login</title>
  </head>
    <body> 
      <h1>Log in</h1>
      <!--Send form input to login.php-->
        <form id="loginForm" method="POST" action="{% url 'login' %}">
            {% csrf_token %}
            <label for="user">Username:</label><br>
            <input type="text" id="username" name="user"><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password"><br>
            <br><input type="submit" value="Log In">
        </form>
      <button><a href="register">Register</a></button>
    </body>
</html>