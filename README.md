# TP Integrador -Organizacion-Empresarial
La empresa TechSolutions S.A. es una empresa dedicada al desarrollo de software. Su área de IT gestiona las solicitudes de equipamiento informático para el personal. <br>
Cuando un empleado necesita un equipo nuevo, debe enviar una solicitud manual. Este procedimiento presenta diversas ineficiencias, tales como demoras en las respuestas, falta de trazabilidad, duplicación de solicitudes y dependencia de la intervención manual de los responsables del área. <br> A partir de un Chatbot desarrollado en Python y SQLite se busca automatizar el proceso de solicitud de equipamiento informático dentro de dicha organización.

## 1. Tecnologías Utilizadas:

-Python 3 <br>
-SQLite <br>
-BPMN 2.0 <br>
-Visual Studio Code <br>

## 2. Modelo BPMN:
<img width="2001" height="436" alt="BPMN Chtabot" src="https://github.com/user-attachments/assets/f22548d2-ea22-433d-8da3-5d4fb83a362f" />


## 3. Diccionario de Datos:

<img width="431" height="585" alt="image" src="https://github.com/user-attachments/assets/9ecfbc9d-b169-422c-ad2d-b620dd6610c0" />

## 4. Manual de Usuario

1. Ejecutar:

`python bot.py`

2. Ingresar número de legajo.

3. Seleccionar equipamiento.

4. El sistema consulta el stock disponible.

5. Se informa el resultado de la solicitud.

### Resultados posibles

- Solicitud aprobada.
- Solicitud pendiente por falta de stock.
- Legajo inexistente.
- Opción inválida.
