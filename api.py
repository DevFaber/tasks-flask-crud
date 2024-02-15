from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id
    data = request.get_json()
    new_task = Task(id=task_id, title=data.get("title"), desc=data.get("desc"))
    task_id += 1
    tasks.append(new_task)
    print(new_task.to_dict())
    return jsonify(new_task.to_dict())

@app.route('/tasks', methods=['GET'])
def read_tasks():
    task_list = [task.to_dict() for task in tasks]  

    out_data = {
        "tasks": task_list,
        "total_tasks": len(task_list)  
    }

    return jsonify(out_data)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for task in tasks:
       if task.id[0] == id:
          return jsonify(task.to_dict())
       
    return jsonify({"message": "Tarefa não encontrada"}), 404


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    updated_task = None
    for task in tasks:
       if task.id[0] == id:
            updated_task = task
            break
       
    if updated_task == None:
        return jsonify({"message":"Tarefa não encontrada"}), 404

    data = request.get_json()
    updated_task.title = data["title"]    
    updated_task.desc = data["desc"]
    updated_task.completed = data["completed"]
    print(updated_task)                 
    return jsonify({"message": "Tarefa atualizada com sucesso"})     


@app.route('/tasks/<int:id>', methods=['DELETE'])
def remove_task(id):
    removed_task = None
    for task in tasks:
        if task.id[0] == id:
            removed_task = task
            break

    if not removed_task:
        return jsonify({'message':'Tarefa não encontrada'}), 404

    tasks.remove(removed_task)
    return jsonify({'message': 'Tarefa deletada com sucesso'})                
                                                 
if __name__ == "__main__" :
  app.run(debug=True)