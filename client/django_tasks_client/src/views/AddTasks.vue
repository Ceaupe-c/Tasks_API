<template>
  <div class="container">
    <div class="add_task">
      <form v-on:submit.prevent="submitForm">
        <div class="form-group">
          <label class="m-4" for="title" id="title">TITULO</label>
          <input type="text" class="form-control" id="title" v-model="title" />
        </div>
        <div class="form-group">
          <label class="m-4" for="description">DESCRIPCION</label>
          <textarea
            class="form-control"
            id="description"
            v-model="description"
          ></textarea>
        </div>
        <div class="form-group">
          <button class="btn btn-success m-4" type="submit">
            Añadir Tarea
          </button>
          <router-link :to="{ name: 'taskcrud' }" id="Home"
            >Ver Tareas</router-link
          >
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {};
  },

  methods: {
    async submitForm() {
      try {
        const response = await axios.post("http://localhost:8000/api/tasks/", {
          title: this.title,
          description: this.description,
          completed: false,
        });
        this.tasks.push(response.data); //Agrega los datos a la matriz de tareas
        this.title = ""; //Restablece los valores de titulo y descripcion
        this.description = "";
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style>
#Home {
  background-color: #111626;
  color: rgb(255, 255, 255);
  border-radius: 5px;
  padding: 10px;
}
</style>