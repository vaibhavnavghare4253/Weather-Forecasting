<!DOCTYPE html>
<html>

<head>
	
</head>

<body>
	<center>
		<?php
		
         // error_reporting(0);
           
            

		// servername => localhost
		// username => root
		// password => empty
		// database name => f_donor
		$conn = mysqli_connect("localhost", "root", "", "wa");
		
		// Check connection
		if($conn === false){
			die("ERROR: Could not connect. "
				. mysqli_connect_error());
		}

          

		// Taking all 5 values from the form data(input)
		 
		$Name = $_REQUEST['Name'];
          
		$Email = $_REQUEST['Email'];
            $Title = $_REQUEST['Title'];
		  $Review = $_REQUEST['Review'];
           
		
		// Performing insert query execution
		// here our table name is donor detail
		$sql = "INSERT INTO waa VALUES ('$Name',
			'$Email','$Title','$Review')";

		
		if(mysqli_query($conn, $sql)){
			echo "<h3>Submit successfully.</h3>";
                  
                 
			echo nl2br("\n$Name \n$Email \n$Title \n$Review"
                 
				);
		} else{
			echo "ERROR: Hush! Sorry $sql. "
				. mysqli_error($conn);
		}
		
		// Close connection
		mysqli_close($conn);
		?>
	</center>
</body>

</html>