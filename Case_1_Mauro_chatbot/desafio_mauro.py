def call_gpt(user_message, gpt_message):
    
    chat_history = []
    
    first_call = True
    
    for user_msg, gpt_msg in zip_longest(user_message, gpt_message, fillvalue = None):
        if user_msg:
            if first_call:
                chat_history.append({"role": "system", "content": user_msg})
                first_call = False
            else:
                chat_history.append({"role": "user", "content": user_msg})
        if gpt_msg:
            chat_history.append({"role": "assistant", "content": gpt_msg})
            
    print(f'Chat history: {chat_history}')
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        # temperature=0.7,
        # max_tokens=150,
        # n=1,
        # stop=None
    )
    
    response_message = response.choices[0].message['content']
    
    return response_message




msg = '' #system message aqui
gpt = ''

user = []
assistant = []

while msg != 'tchau!':
    msg = str(input())
    user.append(msg)
    print('Sua mensagem: {msg}')
    
    gpt = call_gpt(user, assistant) # função que chama o gpt aqui
    print(f'GPT: {gpt}')
    assistant.append(gpt)
    
print('ENCERRADO')

print(f"""{'-' * 20}
Histórico de mensagens:
""")


# Para indice no tamanho da lista de usuários (que é igual a de assistentes)
for indice in range(len(user)):
    print(f'Usuário: {user[indice]}')
    print(f'GPT: {assistant[indice]}')

print(f"{'-' * 20}\n")

# print(user)
# print(assistant)

