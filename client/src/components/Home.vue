<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-4">
        <h2>Ironhack NLP Chat</h2>
      </div>
    </div>
    <div class="row justify-content-center mt-6">
      <div class="col-4">
        <form v-on:submit.prevent="submitForm">
          <div class="form-group">
            <label for="user-name">Chat Name</label>
            <p v-if="userTaken" class="red">
              Name is taken. Please use another.
            </p>
            <input
              v-model="form.name"
              type="text"
              class="form-control"
              id="user-name"
              aria-describedby="user-help"
              placeholder="Enter a chat name"
              required
            />
          </div>
          <div class="form-group">
            <label for="user-name">Age</label>
            <input
              v-model="form.age"
              type="number"
              class="form-control"
              id="user-age"
              aria-describedby="age-help"
              placeholder="Enter your age"
              required
              min="0"
              max="120"
            />
          </div>
          <div class="row">
            <legend class="col-form-label col-sm-2 pt-0">Sex</legend>
            <div class="col-sm-10">
              <div class="form-check">
                <input
                  v-model="form.sex"
                  class="form-check-input"
                  type="radio"
                  name="gridRadios"
                  id="male-radio"
                  value="M"
                  checked
                />
                <label class="form-check-label" for="male-radio">
                  Male
                </label>
              </div>
              <div class="form-check">
                <input
                  v-model="form.sex"
                  class="form-check-input"
                  type="radio"
                  name="gridRadios"
                  id="female-radio"
                  value="F"
                />
                <label class="form-check-label" for="female-radio">
                  Female
                </label>
              </div>
            </div>
          </div>
          <button type="submit" class="btn btn-primary">
            Submit
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",

  mounted() {
    this.isUserLoggedIn();
  },

  data() {
    return {
      userTaken: false,
      form: {
        name: "",
        age: "",
        sex: "M",
        role: 0,
      },
      user: {},
    };
  },
  methods: {
    isUserLoggedIn() {
      var user = localStorage.getItem("user");
      if (user) {
        this.$router.push({ name: "Chats" });
      }
    },
    submitForm() {
      const vm = this;
      this.userTaken = false;
      axios
        .post("api/users", this.form)
        .then((res) => {
          var user = res.data;
          localStorage.setItem("user", JSON.stringify(user));
          vm.$router.push({ name: "Chats" });
        })
        .catch((error) => {
          if (error.response.status == 409) {
            vm.userTaken = true;
          }
        });
    },
  },
};
</script>

<style scoped>
.red {
  color: red;
}
</style>
