from proxmoxer import ProxmoxAPI
import random
import string

# Configuración de la conexión a Proxmox
proxmox = ProxmoxAPI("192.168.1.2", user="api@pve", password="password", verify_ssl=False)

# Generar ID y nombre únicos para el contenedor
def generate_container_id():
    return random.randint(100, 999)  # Genera un ID aleatorio de 3 dígitos

def generate_container_name():
    prefix = "container_"
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))  # Genera una cadena aleatoria de 4 letras minúsculas
    return prefix + suffix

# Parámetros generales para los contenedores
vm_node = "node1"  # Nodo donde se crearán los contenedores
vm_os = "local:vztmpl/debian-11-turnkey-lamp_17.1-1_amd64.tar.gz"  # Sistema operativo de los contenedores (puede ser "debian", "ubuntu", etc.)

# Crear un contenedor
def create_container():
    vm_id = generate_container_id()
    vm_name = generate_container_name()

    proxmox.nodes(vm_node).lxc.create(
        vmid=vm_id,
        ostemplate=vm_os,
        storage="local-lvm",
        #hostname=vm_name,
        memory=512,
        cores=1,
        #net0="virtio,bridge=vmbr0",
        start=1
    )

    print(f"Contenedor '{vm_name}' con ID '{vm_id}' creado exitosamente en el nodo '{vm_node}'.")

# Crear un contenedor individual
create_container()

