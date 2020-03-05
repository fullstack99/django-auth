import * as types from "./mutation-types";

const mutations = {
  [types.LOGIN_SUCCESS](state, data) {
    state.user = data.data.user;
    state.token = data.data.token;
    state.status = data.status;
    state.error = null;
    state.authenticated = true;
  },

  [types.LOGIN_FAILED](state, data) {
    state.user = {};
    state.error = data.data.error;
    state.status = data.status;
    state.authenticated = false;
  },

  [types.REGISTER_SUCCESS](state, data) {
    state.user = data.data.user;
    state.token = data.data.token;
    state.status = data.status;
    state.error = null;
    state.authenticated = true;
  },

  [types.REGISTER_FAILED](state, data) {
    state.user = {};
    state.error = data.data.error;
    state.status = data.status;
    state.authenticated = false;
  },

  [types.AUTH_LOGOUT](state) {
    state.user = {};
    state.error = null;
    state.status = null;
    state.authenticated = false;
    state.token = null;
  }
};

export default mutations;
