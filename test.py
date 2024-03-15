from requests import get, post, delete, put


print(post('http://localhost:5000/api/jobs', json={}).json())

print(post('http://localhost:5000/api/jobs',
           json={'job': 'Заголовок'}).json())

print(post('http://localhost:5000/api/jobs',
           json={'job': 'job',
                'team_leader': 1,
                'worksize': 48,
                'collaborators': '1, 3',
                'is_finished': True}).json())
