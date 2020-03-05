import mutations from "./mutations";
import * as actions from "./actions";
import * as getters from "./getters";

const initialState = {
  user: {},
  error: null,
  status: null,
  authenticated: false,
  token: null
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations
};
