import axios from 'axios';

const BASE = 'http://127.0.0.1:8000/api';

export const api = {
  getModelInfo:        ()       => axios.get(`${BASE}/model-info/`),
  predict:             (data)   => axios.post(`${BASE}/predict/`, data),
  predictBatch:        (list)   => axios.post(`${BASE}/predict-batch/`, { customers: list }),
  getDecisionBoundary: ()       => axios.get(`${BASE}/decision-boundary/`),
  getSampleCustomers:  ()       => axios.get(`${BASE}/sample-customers/`),
  whatIf:              (customer, variable_feature) =>
    axios.post(`${BASE}/what-if/`, { customer, variable_feature }),
};
