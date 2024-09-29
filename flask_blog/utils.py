from itsdangerous import URLSafeTimedSerializer as Serializer

# Use a string for the secret key
s = Serializer(b'secret', 30)

# Generate the token, and remove the decode() call, as dumps() now returns a string in recent versions
token = s.dumps({'user_id': 1})

print(token)
