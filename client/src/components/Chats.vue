<template>
  <div class="row justify-content-center">
    <div class="col-7">
      <div class="detailBox">
        <div class="titleBox">
          <label>Ironhack NLP Chat</label>
        </div>
        <div class="commentBox">
          <p class="taskDescription">
            Each chat is analyzed using natural language processing. The values
            are between -1 and 1.
          </p>
        </div>
        <div class="actionBox">
          <ul class="commentList">
            <li v-for="chat in chats" :key="chat.id">
              <div class="commenterImage">
                <span class="badge" style="color:blue">{{ chat.name }} </span>
              </div>
              <div class="commentText">
                <p class="">{{ chat.message }}</p>
                <br />
                <span class="sentiment"
                  >Sentiment:
                  <span
                    v-if="chat.sentiment > 0.5"
                    class="badge badge-success"
                    >{{ chat.sentiment }}</span
                  >
                  <span
                    v-if="chat.sentiment < -0.5"
                    class="badge badge-danger"
                    >{{ chat.sentiment }}</span
                  >
                  <span
                    v-if="chat.sentiment > -0.5 && chat.sentiment < 0"
                    class="badge badge-warning"
                    >{{ chat.sentiment }}</span
                  >
                  <span
                    v-if="chat.sentiment >= 0 && chat.sentiment < 0.5"
                    class="badge badge-primary"
                    >{{ chat.sentiment }}</span
                  >
                </span>

                <br />
                <span class="date sub-text">{{ chat.created_at }}</span>
              </div>
            </li>
          </ul>
        </div>
        <form class="form-inline" role="form" v-on:submit.prevent="submitForm">
          <div class="form-group">
            <input
              v-model="form.message"
              class="form-control"
              type="text"
              placeholder="Your Message"
              required
              maxlength="200"
              minlength="2"
              max="300"
            />
          </div>
          <div class="form-group">
            <button id="submit-butt" type="submit" class="btn btn-primary">
              Enter
            </button>
          </div>
        </form>
      </div>
    </div>
    <div class="col-2">
      <div class="list-group room">
        <li v-for="user in user_list" :key="user.id" class="list-group-item">
          <span
            >{{ user.name }}:
            <span
              >Average:
              <span v-if="user.mean > 0.5" class="badge badge-success">{{
                user.mean.toFixed(4)
              }}</span>
              <span v-if="user.mean < -0.5" class="badge badge-danger">{{
                user.mean.toFixed(4)
              }}</span>
              <span
                v-if="user.mean > -0.5 && user.mean < 0"
                class="badge badge-warning"
                >{{ user.mean.toFixed(4) }}</span
              >
              <span
                v-if="user.mean >= 0 && user.mean < 0.5"
                class="badge badge-primary"
                >{{ user.mean.toFixed(4) }}</span
              >
            </span>
          </span>
        </li>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Chats",

  mounted() {
    this.interval = setInterval(() => this.getChatData(), 3000);
    this.interval2 = setInterval(() => this.getUsers(), 3000);
  },

  data() {
    return {
      chats: [],
      user_list: null,
      user: JSON.parse(localStorage.getItem("user")),
      form: {
        user_id: null,
        message: "",
      },
    };
  },
  methods: {
    getUsers() {
      const vm = this;
      axios
        .get("http://localhost:5000/api/users")
        .then((res) => {
          vm.user_list = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getChatData() {
      const vm = this;
      axios
        .get("http://localhost:5000/api/chats")
        .then((res) => {
          vm.chats = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    submitForm() {
      const vm = this;
      this.form.user_id = this.user.id;
      if (this.form.message.length < 3) {
        this.form.message = this.form.message + "   ";
      }
      axios
        .post("http://localhost:5000/api/chats", this.form)
        .then((res) => {
          console.log(res.data);
          vm.form.message = "";
        })
        .catch((error) => {
          console.log("ERROR in submit form");
        });
    },
  },
};
</script>

<style lang="css" scoped>
.detailBox {
  width: 100%;
  border: 1px solid #bbb;
}
.titleBox {
  background-color: #fdfdfd;
  padding: 10px;
}
.titleBox label {
  color: #444;
  margin: 0;
  display: inline-block;
}

.commentBox {
  padding: 10px;
  border-top: 1px dotted #bbb;
}
.commentBox .form-group:first-child,
.actionBox .form-group:first-child {
  width: 80%;
}
.commentBox .form-group:nth-child(2),
.actionBox .form-group:nth-child(2) {
  width: 18%;
}
.actionBox .form-group * {
  width: 100%;
}
.taskDescription {
  margin-top: 10px 0;
}
.commentList {
  padding: 0;
  list-style: none;
  max-height: 400px;
  overflow: auto;
  display: flex;
  flex-direction: column-reverse;
}
.commentList li {
  margin: 0;
  margin-top: 10px;
}
.commentList li > div {
  display: table-cell;
}
.commenterImage {
  width: 30px;
  margin-right: 5px;
  height: 100%;
  float: left;
}
.commenterImage img {
  width: 100%;
  border-radius: 10%;
}
.commentText p {
  margin: 0;
  margin-left: 50px;
}
.sub-text {
  color: #aaa;
  font-family: verdana;
  font-size: 11px;
  margin: 0;
  margin-left: 50px;
}
.sentiment {
  margin-left: 50px;
}
.actionBox {
  border-top: 1px dotted #bbb;
  padding: 10px;
}

input[type="text"] {
  width: 500px;
}

#submit-butt {
  margin-left: 30px;
}

.room {
  padding: 0;
  list-style: none;
  max-height: 588px;
  overflow: auto;
}
</style>
