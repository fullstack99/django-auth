import axios from "axios";
import * as types from "./mutation-types";
// import apiService from '@/api/api.service'
import { API_URL } from "@/lib/config";

export const login = ({ commit }, data) => {
  return axios.post(`${API_URL}login`, data)
    .then(res => {
      commit(types.LOGIN_SUCCESS, res);
      localStorage.setItem("accesstoken", res.data.token);
      return res;
    })
    .catch(err => {
      commit(types.LOGIN_FAILED, err.response);
      return err.response;
    });
};

export const register = ({ commit }, data) => {
  return axios.post(`${API_URL}register`, data)
    .then(res => {
      commit(types.REGISTER_SUCCESS, res);
      localStorage.setItem("accesstoken", res.data.token);
      return res;
    })
    .catch(err => {
      commit(types.REGISTER_FAILED, err.response);
      return err.response;
    });
};

export const logout = ({ commit }) => {
  localStorage.removeItem("user");
  localStorage.removeItem("accesstoken");
  localStorage.removeItem("currentUser");

  commit(types.AUTH_LOGOUT);
};
