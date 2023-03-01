import React, {useState} from "react"
import './Login.css'
import { Form, Input, Button, Checkbox } from 'antd';
import {LockOutlined, UserOutlined} from '@ant-design/icons'
import makeAPIRequest from "../../utils/makeAPIRequest";

const token = localStorage.getItem("token");

const Login = () => {
  const [formData, setFormData] = useState({
    username: "",
    password: ""
  })

  const onSubmit = () => {
    localStorage.removeItem("token")
    makeAPIRequest({
      url:"http://localhost:8000/auth-token/",
      method:"POST",
      params:{
        "username": formData.username,
        "password": formData.password
      },
      callback: (resp) => {
        localStorage.setItem("token", resp.token)
        if(resp.token == undefined){
          alert("Failed Login")
        }
        else{
          alert("Successful Login")
        }
      },
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`
      }
    });
  };

  const onSubmitFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return(
    <Form className="login-form" onFinish={onSubmit}  onFinishFailed={onSubmitFailed} autoComplete="off">
      <h1 className="form-title">Login</h1>
      {/* Username */}
      <Form.Item
        name="username"
        rules={[{ required: true, message: 'Username required' }]}
      >
        <Input
          prefix={<UserOutlined style={{ color: 'rgba(0,0,0,.25)' }} />} 
          type="username"
          placeholder="Username"
          onChange={(e) => setFormData({...formData, username: e.target.value})} 
          value={formData.username} 
        />
      </Form.Item>
      {/* Password */}
      <Form.Item
        name="password"
        rules={[{ required: true, message: 'Password required' }]}
      >
        <Input
          prefix={<LockOutlined style={{ color: 'rgba(0,0,0,.25)' }} />} 
          type="password"
          placeholder="Password"
          onChange={(e) => setFormData({...formData, password: e.target.value})} 
          value={formData.password} 
        />
      </Form.Item>
      <Form.Item>
      <Checkbox>Remember me</Checkbox>
          <a className="login-form-forgot" href="">
            Forgot password
          </a>
        <Button
            type="primary"
            htmlType="submit"
            className="login-form-button"
          >
            Login
        </Button>
        <div>New Here? <a href="">Sign Up</a></div>
      </Form.Item>
    </Form>
  )
}

export default Login