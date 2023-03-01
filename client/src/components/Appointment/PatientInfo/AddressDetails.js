import React, {useState} from "react"
import "./PatientInfo.css"
import { Row, Col, Form, Input, Select, DatePicker } from 'antd';
import {UserOutlined, PhoneOutlined, MailOutlined, PushpinOutlined} from '@ant-design/icons'

const { Option } = Select;


const AddressDetails = () => {
    const [formData, setFormData] = useState({
        address1: "",
        address2: "",
        villageWard: "",
        city: "",
        country: "",
        
      });
    
return (
    <div className="wrapper">
        {/* Ribbon */}
        <div className="ribbon ribbon-top-right"><span>Patient</span></div>

        <div className="address-details">
        <div className="section-label">Address Details</div>
            <Row>
                <Col span={12} style={{ textAlign: 'left' }}>
                    {/* Address Line 1*/}
                    <Form.Item 
                        label="Address 1" 
                        name="address1" 
                        rules={[{ required: true, message: 'Address Line 1 is required' }]}>
                        <Input.TextArea 
                            placeholder="Address Line 1"
                            onChange={(e) => setFormData({...formData, address1: e.target.value})} 
                            value={formData.address1} 
                        />
                    </Form.Item>
                </Col>
                    
                    {/* Address Line 2 */}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item
                        label="Address Line 2"
                        name="address2">
                        <Input.TextArea 
                            placeholder="Address Line 2"
                            value={formData.address2} 
                        />
                    </Form.Item>
                </Col>
            </Row>

            <Row>
                {/* Village/Ward */}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item
                        label="Village/Ward"
                        name="villageWard"
                        rules={[{ required: true, message: 'Village/Ward is required' }]}
                    >
                        <Input
                            prefix={<PushpinOutlined  style={{ color: 'rgba(0,0,0,.25)' }} />} 
                            type="villageWard"
                            placeholder="Village/Ward"
                            onChange={(e) => setFormData({...formData, villageWard: e.target.value})} 
                            value={formData.villageWard} 
                            />
                    </Form.Item>
                </Col>

                {/* City */}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item
                        label="City"
                        name="city"
                        rules={[{ required: true, message: 'City is required' }]}
                    >
                        <Input
                            prefix={<PushpinOutlined  style={{ color: 'rgba(0,0,0,.25)' }} />} 
                            type="city"
                            placeholder="City"
                            onChange={(e) => setFormData({...formData, city: e.target.value})} 
                            value={formData.city} 
                            />
                    </Form.Item>
                </Col> 
            </Row>

            <Row>
                {/* Country */}
                <Col span={12} style={{ textAlign: 'left' }}>
                    <Form.Item
                        label="Country"
                        name="country"
                        rules={[{ required: true, message: 'Country is required' }]}
                    >
                        <Select placeholder="Select Country">
                            <Option value="guyana">Guyana</Option>
                        </Select>
                    </Form.Item>
                </Col>  
            </Row>

        </div>
    </div>
    )
}

export default AddressDetails