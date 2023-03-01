import React, {useState} from "react"
import "./Appointment.css"
import {Form, Button} from 'antd';
import PersonalDetails from "./PatientInfo/PersonalDetails"
import AddressDetails from "./PatientInfo/AddressDetails"
import AppointmentDetails from "../Appointment/AppointmentInfo/AppointmentDetails"


const layout = {
    labelCol: {
      span: 10,
    },
    wrapperCol: {
      span: 16,
    },
  };


const Appointment = (props) => {
    const [page, setPage] = useState(0);
    const [form] = Form.useForm()

    const componentList = [
      <PersonalDetails
        // formData={formData}
        // setFormData={setFormData}
        page={page}
        setPage={setPage}
       />,
       <AddressDetails
      //  formData={formData}
      //  setFormData={setFormData}
       page={page}
       setPage={setPage}
      />,
      <AppointmentDetails
      // formData={formData}
      // setFormData={setFormData}
      page={page}
      setPage={setPage}
     />,
    ];

    const validateFields = (btnName) => {
      form.validateFields()
      .then(() => setPage(page + 1))
      .catch((error) => console.log(error.errorFields.length + ' Error Field(s) Exist:', error.errorFields))
    };

    const onFinish = (e) => {
      e.preventDefault();
      console.log(e)
    };  

    return (
        <Form className="appointment-form" form={form} onFinish={onFinish}  autoComplete="off" {...layout}>
            <h1 className="form-title">Appointment Form</h1>
            <div style={{textAlign: "right"}}>{componentList[page]}
                {page > 0 && (
                    <Button
                        htmlType="button"
                        className="prev-btn"
                        onClick={() => setPage(page - 1)}>
                        Previous
                    </Button>
                )}
                {page == 2 && (
                  <Button
                      type="primary"
                      htmlType="submit"
                      className="submit-btn">
                      Submit
                  </Button>                    
                )}
                {page <= 1 && (
                    <Button
                        type="primary"
                        htmlType="button"
                        className="next-btn"
                        onClick={() => validateFields()}>
                        Next
                    </Button>
                )}

           </div>
        </Form>
    )
}

export default Appointment