from itsdangerous import URLSafeTimedSerializer as Serializer


s = Serializer(b'secret', 30)


token = s.dumps({'user_id': 1})

print(token)
