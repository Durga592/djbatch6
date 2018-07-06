# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def temprature(temprature):
	return HttpResponse("hello")

def student_reg_form(request):
	return render(request,"cooling/student_course_details.html")

def student_reg_form1(request):
	return render(request,"cooling1/student_course_details.html")

def student_reg_form2(request):
	return render(request,"cooling2/student_course_details.html")

def student_reg_form3(request):
	return render(request,"cooling3/student_course_details.html")

def student_reg_form4(request):
	return render(request,"cooling4/student_course_details.html")

def student_reg_form5(request):
	return render(request,"cooling5/student_course_details.html")

def courseregistrationform(request):
	data = """
			<!DOCTYPE html>
<html>
<head>
	<title>STUDENT COURSE DETAILS</title>
</head>
<body>
	<form mathod="POST">
	
	<table cellpadding="2" width="20%" bgcolor="99FFFF" align="center"

	  cellspacing="2">
	<tr>

	  <td colspan=2>

	  <center><font size=4><b>Student Registration Form</b></font></center>

	  </td>

	  </tr>

	<tr>

	  <td>Name</td>

	  <td><input type=text name=textnames id="textname" size="30"></td>

	  </tr>

	<tr>

	  <td>Father Name</td>

	  <td><input type="text" name="fathername" id="fathername"

	  size="30"></td>

	  </tr>

	  <tr>

	  <td>Postal Address</td>

	  <td><input type="text" name="paddress" id="paddress" size="30"></td>

	  </tr>

	<tr>

	  <td>Personal Address</td>

	  <td><input type="text" name="personaladdress"

	  id="personaladdress" size="30"></td>

	  </tr>

	<tr>

	  <td>Sex</td>

	  <td><input type="radio" name="sex" value="male" size="10">Male

	  <input type="radio" name="sex" value="Female" size="10">Female</td>

	  </tr>

	<tr>

	  <td>City</td>

	  <td><select name="City">

	  <option value="-1" selected>select..</option>

	  <option value="New Delhi">NEW DELHI</option>

	  <option value="Mumbai">MUMBAI</option>

	  <option value="Goa">GOA</option>

	  <option value="Patna">PATNA</option>

	  </select></td>

	  </tr>

	<tr>

	  <td>Course</td>

	  <td><select name="Course">

	  <option value="-1" selected>select..</option>

	  <option value="Python">Python</option>

	  <option value="Django">Django</option>

	  <option value="IOT">IOT</option>

	  <option value="DataScience">DataScience</option>

	  </select></td>

	  </tr>

	<tr>

	  <td>District</td>

	  <td><select name="District">

	  <option value="-1" selected>select..</option>

	  <option value="Nalanda">NALANDA</option>

	  <option value="UP">UP</option>

	  <option value="Goa">GOA</option>

	  <option value="Patna">PATNA</option>

	  </select></td>

	</tr>

	<tr>

	  <td>State</td>

	  <td><select Name="State">

	  <option value="-1" selected>select..</option>

	  <option value="New Delhi">NEW DELHI</option>

	  <option value="Mumbai">MUMBAI</option>

	  <option value="Goa">GOA</option>

	  <option value="Bihar">BIHAR</option>

	  </select></td>

	  </tr>

	  <tr>

	  <td>PinCode</td>

	  <td><input type="text" name="pincode" id="pincode" size="30"></td>

	</tr>

	  <tr>

	  <td>EmailId</td>

	  <td><input type="text" name="emailid" id="emailid" size="30"></td>

	  </tr>

	<tr>

	  <td>DOB</td>

	  <td><input type="text" name="dob" id="dob" size="30"></td>

	  </tr>

	<tr>

	  <td>MobileNo</td>

	  <td><input type="text" name="mobileno" id="mobileno" size="30"></td>

	  </tr>

	  <tr>

	  <td><input type="reset"></td>

	  <td colspan="2"><input type="submit" name="" svalue="Submit Form" /></td>

	  </tr>

	  </table>

	  </form>
</body>
</html>	
	"""
	return HttpResponse(data)