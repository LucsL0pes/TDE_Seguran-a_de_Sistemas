Criptografia - AES e modos de operação

Escola Politécnica/PUCRS

Durante a análise de um servidor comprometido, cinco mensagens criptografadas foram
encontradas. As mensagens utilizam AES nos modos CBC e CTR. Seu desafio é decifrar
corretamente quatro dessas mensagens usando as informações disponíveis.
Abaixo estão os dados e as chaves para o AES, além do texto cifrado. Sua tarefa é
recuperar o texto claro para aqueles que estão cifrados e cifrar o texto claro solicitado em
“Tarefas a serem realizadas”. Todos os textos cifrados estão em hexadecimal. Para a
implementação pode-se utilizer qualquer linguagem que forneça uma biblioteca para o
AES, por exemplo, PyCrypto (Python), Crypto++ (C++), Java.
Submeter sua implementação e um artigo com até duas páginas com sua solução e as
respostas.
O que deve ser submetido
1. Decifrar corretamente a lista de tarefas que segue.
2. Identificar qual das mensagens contém a “FLAG”.
3. Criptografar uma mensagem, cujo texto claro deve conter o nome completo dos
integrantes do trabalho. A criptografia deve ser feita com AES, usando o mesmo
modo de operação e chave utilizada para a mensagem que contém a FLAG.
O que deve estar contido no artigo
- Apresenta como a solução foi modelada
- Como você identificou e decifrou cada mensagem
- Sobre a solução
- Indique como ela funciona
- Indique como deve-se compilar a solução
- Deve-se usar o github como repositório, o qual deverá ser indicado no artigo
- Mantenham o repositório privado e incluam o usuário empucrs para ter
acesso ao recurso elaborado
- Indique:
- Os modos de operação usados em cada tarefa
- Os textos decifrados de cada texto cifrado
- Qual tarefa contém a FLAG
- Como foi elaborada a solução de criptografia
Tarefa 1
• CBC Key: d50a3bb2c2811dd860ed0b344867b406
• Ciphertext:
38f726acdccedb7953e4fc4e16f3035a3dd2581511cfaa3a7f0b12df725784cc2fc367ca81193c189845443171
3c3422371e82e3cb64d95bc4263c08062662e3
Tarefa 2
• CBC Key: d50a3bb2c2811dd860ed0b344867b406
• Ciphertext:
203c6bac6f9cf76ebecde621eb7615f9a7773dbfb6e20d75d78d2b7683d25597712190f6f6faf662dcd75b8415
66a134608ae5b0520d295c05142b42a9f887bd3edddacacf4f3e3b0c4b7849695d46d9
Tarefa 3
• CTR Key: 1fbf6bebb2f7f365b00a4bdad4d0a4ac
• Ciphertext:
4db4a169a55cf550ada23592edae27885f8b26d6ebba3a3f8bf6977cc5a25982bbb72d6e0183676b138a9ecf8
91c444587e77ae07b2f638ecf2ee5c6cd
Tarefa 4
• CTR Key: 1fbf6bebb2f7f365b00a4bdad4d0a4ac
• Ciphertext:
267b0a4cea65edd43a43ca29990ac0da7659f392fcf5de0e4e32d065de9de5afad8bca61e0369cf8da72765078
59a4ce8ba8fadbce5e5d1eb55c0f5875e752c723dd685a3b0d
