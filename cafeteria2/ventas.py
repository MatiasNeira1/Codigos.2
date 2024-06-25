import json
import random
import globales


def precargar_ventas():
    ventas = globales.leer_archivo_json("ventas.json")
    empleados = globales.leer_archivo_json("empleados.json")

    id_venta = 1

    for i in range(10):

        empleado = random.choice(empleados)

        id_venta += 1
        id_empleado = empleado["id_empleado"]
        total_venta = random.randint(30000, 70000)
        propina = total_venta * 0.1

        nueva_venta_aleatoria = {
            "id_venta": id_venta,
            "id_empleado": id_empleado,
            "total_venta": total_venta,
            "propina": propina,
        }

        ventas.append(nueva_venta_aleatoria)

    globales.guardar_archivo_json("ventas.json", ventas)
