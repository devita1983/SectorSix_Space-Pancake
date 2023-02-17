# SectorSix_Space-Pancake
Projeto em Python que utiliza a biblioteca 'astroquery.mast' e a biblioteca 'astropy' para buscar imagens do setor 6 do satélite TESS da NASA

"Este é um projeto em Python que utiliza a biblioteca 'astroquery.mast' e a biblioteca 'astropy' para buscar imagens do setor 6 do satélite TESS da NASA que cobrem um objeto celeste em particular.

Usando este código, você pode definir as coordenadas do objeto de interesse e buscar os setores do TESS que cobrem essas coordenadas usando o método 'get_sectors'. Em seguida, é possível verificar se o setor desejado está presente usando o método 'get_cutouts'. Se o objeto estiver no setor, você pode recuperar uma imagem do objeto usando 'get_cutouts'. A imagem é então plotada usando a biblioteca 'matplotlib'.

Este código pode ser útil para astrônomos e entusiastas da astronomia que desejam explorar as possibilidades da análise de dados astronômicos com Python. É possível modificar este código para analisar outros objetos celestes em diferentes setores do TESS, o que pode levar a novas descobertas em astrofísica.

Sinta-se à vontade para baixar e explorar o código por conta própria. Qualquer feedback ou contribuição será bem-vindo!"

# Requisitos

Para executar o código, você precisará dos seguintes pacotes instalados:

* astroquery
* astropy
* matplotlib

Você pode instalá-los usando o gerenciador de pacotes pip:

![image](https://user-images.githubusercontent.com/117879893/219801133-b25d4239-aa34-4e8e-a8f0-442d4da5c5af.png)

# Instruções

* 1. Clone este repositório para o seu computador.
* 2. Abra o arquivo 'tesscut_example.py' em um editor de texto ou ambiente de desenvolvimento Python.
* 3. Edite as variáveis 'ra', 'dec' e 'sector' para definir as coordenadas do objeto de interesse e o setor TESS desejado.
* 4. Execute o arquivo 'tesscut_example.py' usando o comando 'python tesscut_example.py'.
* 5. Se o objeto estiver no setor, uma imagem do objeto será plotada usando a biblioteca 'matplotlib'.

# Exemplo

Um exemplo de como usar o código pode ser encontrado no arquivo tesscut_example.ipynb. Neste notebook Jupyter, você pode ver um exemplo completo de como usar o código para buscar imagens do TESS para um objeto celeste específico.

Sinta-se à vontade para baixar e explorar o código por conta própria. Qualquer feedback ou contribuição será bem-vindo!

Para entrar em contato envie um email para lcd@eikocloud.com 











