import * as types from "./mutation-types";

const mutations = {
  [types.LOGIN_SUCCESS](state, data) {
    state.user = data.data.user;
    state.token = data.data.token;
    state.status = data.status;
    state.error = null
  },

  [types.LOGIN_FAILED](state, data) {
    state.user = {};
    state.error = data.data.error;
    state.status = data.status;
  },

  [types.REGISTER_SUCCESS](state, data) {
    state.user = data.data.user;
    state.token = data.data.token;
    state.status = data.status;
    state.error = null
  },

  [types.REGISTER_FAILED](state, data) {
    state.user = {};
    state.error = data.data.error;
    state.status = data.status;
  },
}

export default mutations;