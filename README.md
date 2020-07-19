# Paper-Pro

This is a Django Project developed with the default sqlite backend. It was developed for a college project work.<br>
Steps for execution <br>
<ol>1. Navigate to the CT folder</ol>
<ol>2. Edit the settings file. You will have to update the email address for the smtp server and file paths</ol>
<ol>3. Run python manage.py makemigrations </ol>
<ol>4. Run python manage.py migrate</ol>
<ol>5. Launch the website by running python manage.py runserver.</ol>

If you are adding any new static files then you must run the command python manage.py collectstatic before launching the website.

<h2>How to use the website</h2>
There are four user groups in this project. <br>
Author: the person who uploads papers for the conference. This account can be created through the login/signup page in the website <br>
Reviewer: the person who reviews papers and gives comments on them <br>
Editor: one of the core members of the conference managing team. The editor can view all the papers that have been submitted and assigns them to the reviewer. The editor can also see the comments from the reviewers and is the final decision maker on whether the paper can be accepted or not. <br>
Admin: the Django superuser. Manages the entire website. Has access to the database <strong>Only the admin can create the reviewer and editor profiles. They cannot be created through normal login or signup. </strong>
  
<h3>How to start </h3>
<ol>1. First create the superuser using the command python manage.py createsuperuser</ol>
<ol>2. Login to the django admin interface and create the editor and reviewer profiles</ol>
<ol>3. Create the author profile from the website interface. </ol>
<ol>4. Login to the author's account and upload a paper in pdf format. Once the paper has been uploaded the color of the bar changes to yellow</ol>
<ol>5. Login to the editor's account and assign a reviewer for the paper</ol>
<ol>6. Login to the reviewer's account and view the paper and give comments to the editor and author regarding the paper</ol>
<ol>7. If the paper needs changes then the author can make them based on the comments and use the update paper option. Based on the reviewer's suggestions the editor can accept/reject the paper the paper. Based on the accept/reject the color of the bar changes to green or red.</ol>
