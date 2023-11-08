import json

API_TOKEN = "123"

def lambda_handler(event, context):
    if event.get('httpMethod') == 'POST':
        authorization_header = event.get('headers', {}).get('Authorization')
        if authorization_header is None or authorization_header != f'Bearer {API_TOKEN}':
            return {
                'statusCode': 401,
                'body': json.dumps('Falha na autenticação ou método não permitido')
            }
        
        if 'body' in event:
            try:
                request_body = json.loads(event['body'])
                response_body = 'Autenticado com sucesso e processado com êxito'
                return {
                    'statusCode': 200,
                    'body': json.dumps(response_body)
                }
            except json.JSONDecodeError as e:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Erro na decodificação JSON: ' + str(e))
                }

    return {
        'statusCode': 400,
        'body': json.dumps('Solicitação inválida')
    }
