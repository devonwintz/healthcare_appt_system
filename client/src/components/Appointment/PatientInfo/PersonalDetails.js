import React, {useState} from "react"
import "./PatientInfo.css"
import { Row, Col, Form, Input, Select, DatePicker } from 'antd';
import {UserOutlined, PhoneOutlined, MailOutlined} from '@ant-design/icons'

const { Option } = Select;


const PatientInfo = () => {
    const [formData, setFormData] = useState({
        firstName: "",
        lastName: "",
        sex: "",
        telephone: "",
        email: ""
      });
    
return (
    <div className="wrapper">
        {/* Ribbon */}
        <div className="ribbon ribbon-top-right"><span>Patient</span></div>
        <div className="personal-details">
        <div className="section-label">Personal Details</div>
            <Row>
                {/* First Name */}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item
                        label="First Name"
                        name="firstName"
                        rules={[{ required: true, message: 'First Name is required'}]}
                    >
                        <Input
                            prefix={<UserOutlined  style={{ color: 'rgba(0,0,0,.25)' }} />} 
                            type="firstName"
                            placeholder="First Name"
                            onChange={(e) => setFormData({...formData, firstName: e.target.value})} 
                            value={formData.firstName} 
                            />
                    </Form.Item>
                </Col> 

                {/* Last Name */}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item
                        label="Last Name"
                        name="lastName"
                        rules={[{ required: true, message: 'Last Name is required' }]}
                    >
                        <Input
                            prefix={<UserOutlined  style={{ color: 'rgba(0,0,0,.25)' }} />} 
                            type="lastName"
                            placeholder="Last Name"
                            onChange={(e) => setFormData({...formData, lastName: e.target.value})} 
                            value={formData.lastName} 
                            />
                    </Form.Item>
                </Col>               
            </Row>

            <Row>
                {/* Sex */}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item
                        label="Sex"
                        name="sex"
                        rules={[{ required: true, message: 'Sex is required' }]}
                    >
                    <Select 
                        placeholder="Select Sex" 
                        onChange={(e) => setFormData({...formData, sex: e.target.value})} 
                    >
                        <Option value="male">Male</Option>
                        <Option value="female">Female</Option>
                    </Select>
                    </Form.Item>
                </Col>

                {/* Date of Birth*/}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item 
                        label="Birth Date" 
                        name="dob" 
                        rules={[{ required: true, message: 'DOB is required' }]}>
                        <DatePicker format="YYYY-MM-DD" style={{width: '100%'}}/>
                    </Form.Item>
                </Col>
            </Row>

            <Row>
                {/* Telephone */}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item
                        label="Telephone"
                        name="telephone"
                    >
                        <Input
                            prefix={<PhoneOutlined  style={{ color: 'rgba(0,0,0,.25)' }} />} 
                            type="telephone"
                            placeholder="Telephone"
                            onChange={(e) => setFormData({...formData, telephone: e.target.value})} 
                            value={formData.telephone} 
                            />
                    </Form.Item>
                </Col>

                {/* Email */}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item
                        label="Email"
                        name="email"
                    >
                        <Input
                            prefix={<MailOutlined  style={{ color: 'rgba(0,0,0,.25)' }} />} 
                            type="email"
                            placeholder="Email"
                            onChange={(e) => setFormData({...formData, email: e.target.value})} 
                            value={formData.email} 
                            />
                    </Form.Item>
                </Col> 
            </Row>
        </div>
    </div>
    )
}

export default PatientInfo
