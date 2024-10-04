from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

subject = "hello"
from_email = 'no-reply@blancexchange.net'
to = "kezechristian@gmail.com"

# Load the HTML template and render it with context (if needed)
html_content = render_to_string('activate.html', {'some_context_variable': 'some_value'})

# Create the email message
msg = EmailMultiAlternatives(subject, None, from_email, [to])

# Attach the HTML content to the message
msg.attach_alternative(html_content, "text/html")

# Send the email
msg.send()
