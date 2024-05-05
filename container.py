
class ContainerStack:
    def __init__(self):
        self.stacks = [[] for _ in range(4)]  # Inicializa 4 pilhas vazias

    def push(self, container_id):
        # Encontra a pilha com a menor quantidade de containers e adiciona o novo container
        min_stack = min(self.stacks, key=len)
        if len(min_stack) < 3:
            min_stack.append(container_id)
        else:
            print("Impossível empilhar: não há mais espaço disponível nas pilhas.")

    def pop(self, container_id):
        # Encontra a pilha que contém o container e verifica se ele está no topo
        for stack in self.stacks:
            if stack and stack[-1] == container_id:
                stack.pop()
                return
        print("Impossível desempilhar: o container não está no topo de nenhuma pilha ou não existe.")

# Exemplo de uso
if __name__ == "__main__":
    container_stack = ContainerStack()
    container_stack.push("C001")
    container_stack.push("C002")
    container_stack.push("C003")
    container_stack.push("C004")
    container_stack.pop("C004")
