<template>
  <div class="container">
    <!-- breakpoint -->
    <h1>Tareas</h1>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="task in tasks" :key="task.id">
        <div class="col">
          <div class="card m-3">
            <div class="card-body">
              <h4 class="card-title d-flex justify-content-center">
                {{ task.title }}
              </h4>
              <p class="card-text">{{ task.description }}</p>
              <button @click="toggleTask(task)">
                {{ task.completed ? "Undo" : "Complete" }}
              </button>
              <button @click="deleteTask(task)">Eliminar</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="add_task">
      <form v-on:submit.prevent="submitForm">
        <div class="form-group">
          <label for="title" id="title">Titulo</label>
          <input type="text" class="form-control" id="title" v-model="title" />
        </div>
        <div class="form-group">
          <label for="description">Descripcion</label>
          <textarea
            class="form-control"
            id="description"
            v-model="description"
          ></textarea>
        </div>
        <div class="form-group">
          <button type="submit">Añadir Tarea</button>
        </div>
      </form>
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
        this.tasks = await response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async submitForm() {
      try {
        const response = await axios.post("http://localhost:8000/api/tasks/", {
          title: this.title,
          description: this.description,
          completed: false,
        });
        this.tasks.push(response.data);
        this.title = "";
        this.description = "";
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

        let taskIndex = this.tasks.findIndex((t) => t.id === task.id);

        this.tasks = this.tasks.map((task) => {
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
      let confirmation = confirm("Quieres eliminar esta tarea?");

      if (confirmation) {
        try {
          await axios.delete(`http://localhost:8000/api/tasks/${task.id}`);

          this.getData();
        } catch (error) {
          console.log(error);
        }
      }
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style>
.navbar-light {
  color: #111626;
}
</style>