import React, {useState} from "react"
import "./AppointmentDetails.css"
import { Row, Col, Form, Select, DatePicker, TimePicker  } from 'antd';

const { Option } = Select;
const { RangePicker } = TimePicker;


const AppointmentDetails = () => {
    const [formData, setFormData] = useState({
        category: "",
        doctor: "",
        date: "",
        time: "",   
      });

      const range = (start, end) => {
        const result = [];
        for (let i = start; i < end; i++) {
          result.push(i);
        }
        return result;
      }

    // This needs to be made dynamic
    const disabledRangeTime = (_, type) => {
    if (type === 'start') {
        return {
        disabledHours: () => range(0, 60).splice(4, 20),
        disabledMinutes: () => range(30, 60),
        disabledSeconds: () => [55, 56],
        };
    }
    else{
        return {
            disabledHours: () => range(0, 60).splice(20, 4),
            disabledMinutes: () => range(0, 31),
            disabledSeconds: () => [55, 56],
        };
    }
    }
    
return (
    <div>
        {/* Ribbon */}
        <div class="ribbon ribbon-top-right"><span>Appointment</span></div>
        <div className="wrapper">
            <div className="doctor-details">
            <div className="section-label">Doctor Details</div>
                <Row>
                    {/* Doctor Specialization */}
                    <Col span={12} style={{ textAlign: 'left' }}>
                        <Form.Item
                            label="Category"
                            name="category"
                            rules={[{ required: true, message: 'Category is required' }]}
                        >
                        <Select 
                            placeholder="Select Category" 
                            onChange={(e) => setFormData({...formData, category: e.target.value})} 
                        >
                            <Option value="dermatology">Dermatology</Option>
                        </Select>
                        </Form.Item>
                    </Col>

                    {/* Doctor */}
                    <Col span={12} style={{ textAlign: 'left' }}>
                        <Form.Item
                            label="Doctor"
                            name="doctor"
                            rules={[{ required: true, message: 'Doctor is required' }]}
                        >
                        <Select 
                            placeholder="Select Doctor"
                            onChange={(e) => setFormData({...formData, doctor: e.target.value})} 
                        >
                            <Option value="doctor1">Doctor 1</Option>
                        </Select>
                        </Form.Item>
                    </Col>
                </Row>
                
                <div className="section-label">Appointment Details</div> 
                <Row>
                    {/* Date */}
                    <Col span={12} style={{ textAlign: 'left' }}>
                        <Form.Item
                            label="Date"
                            name="date"
                            rules={[{ required: true, message: 'Date is required' }]}
                        >
                            <DatePicker 
                                format="YYYY-MM-DD" 
                                style={{width: '100%'}}
                                onChange={(e) => setFormData({...formData, date: e.target.value})} 
                            />
                        </Form.Item>
                    </Col>

                    {/* Time */}
                    <Col span={12} style={{ textAlign: 'left' }}>
                        <Form.Item 
                            label="Time" 
                            name="time" 
                            rules={[{ required: true, message: 'Time is required' }]}>
                            {/* <TimePicker defaultOpenValue={dayjs('00:00:00', 'HH:mm:ss')} style={{width: '100%'}} /> */}
                            <RangePicker 
                                style={{width: '100%'}} 
                                onChange={(e) => setFormData({...formData, time: e.target.value})} 
                                disabledTime={disabledRangeTime}
                            />
                        </Form.Item>
                </Col>
                </Row>
            </div>
            </div>
        </div>
    )
}

export default AppointmentDetails