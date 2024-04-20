import requests

def read_and_post_users(file_path, api_url="http://localhost:5000/pedidos"):
  
    pedidos_add = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                usuario_id, descricao, status, id_produto = line.strip().split('; ')

                data = {
                    "usuario_id": usuario_id,
                    "descricao": descricao,
                    "status": status,
                    "id_produto": id_produto
                }

                response = requests.post(api_url, json=data)

                if response.status_code == 201:
                    pedidos_add += 1
                    print(f"Pedidos adicionados: {descricao}")  # Print success message

    except Exception as error:
        print(f"Erro ao adicionar: {str(error)}")

    return pedidos_add

# Example usage (replace with your actual file path)
pedidos_add = read_and_post_users("order.txt")
print(f"{pedidos_add} Pedidos adicionados")


