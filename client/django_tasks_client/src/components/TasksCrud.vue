<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark p-3">
      <router-link :to="{ name: 'addtasks' }"> Añadir Tarea </router-link>
    </nav>
    <div class="container">
      <!-- breakpoint -->
      <h1 id="h-title">Tareas</h1>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div v-for="task in tasks" :key="task.id">
          <div class="col">
            <div class="card text-white bg-dark m-3">
              <div class="card-body">
                <h4 class="card-title d-flex justify-content-center">
                  {{ task.title }}
                </h4>
                <p class="card-text">{{ task.description }}</p>
                <button class="btn btn-success" @click="toggleTask(task)">
                  {{ task.completed ? "Completa" : "Incompleta" }}
                </button>
                <button class="btn btn-danger m-1" @click="deleteTask(task)">
                  Eliminar
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      tasks: [],
      title: "",
      description: "",
    };
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get("http://localhost:8000/api/tasks/");
        this.tasks = response.data; //Establece los datos devueltos como tareas
      } catch (error) {
        console.log(error);
      }
    },
    async toggleTask(task) {
      try {
        const response = await axios.put(
          `http://localhost:8000/api/tasks/${task.id}`,
          {
            completed: !task.completed,
            title: task.title,
            description: task.description,
          }
        );

        let taskIndex = this.tasks.findIndex((t) => t.id === task.id); //Obtencion del indice de la tarea que se está actualizando

        this.tasks = this.tasks.map((task) => { //Recorre el array de tareas y actualiza el nuevo estado de la tarea
          if (this.tasks.findIndex((t) => t.id === task.id) === taskIndex) {
            return response.data;
          }
          return task;
        });
      } catch (error) {
        console.log(error);
      }
    },

    //eslint-disable-next-line no-unused-vars
    async deleteTask(task) {
      let confirmation = confirm("Quieres eliminar esta tarea?"); //Alert confirmando si se quiere o no eliminar la tarea

      if (confirmation) {
        try {
          await axios.delete(`http://localhost:8000/api/tasks/${task.id}`); //Request de eliminar tarea

          this.getData(); //Actualiza las tareas
        } catch (error) {
          console.log(error);
        }
      }
    },
  },
  created() {
    this.getData(); //Obtencion de tareas al recargar la página 
  },
};
</script>

<style>
#h-title {
  color: azure;
  padding-top: 20px;
}
</style>