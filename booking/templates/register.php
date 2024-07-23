<!DOCTYPE html>
<html lang='en'>
<title>Register</title>
  </head>
    <body>
      <h1>Register</h1>
      <!--Send form input to login.php-->
        <form  id="RegistrationForm" method="POST" action='includes/registration.php'>{%csrf_token %}
            <label for="user">Email:</label><br>
            <input type="text" id="email" name="user"><br>
            <label for="user">Username:</label><br>
            <input type="text" id="username" name="user"><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password">
            <label for="password">Confirm Password:</label>
            <input type="password" id="confirm password" name="password">
<br>
            <input type="submit" value="Register">
          <button><a href="{% url 'index' %}?next={{ request.path }}">Login</a></button>
        </form>
    </body>
</html>