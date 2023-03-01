import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Login from "./components/Login/Login"
import Appointment from "./components/Appointment/Appointment"
import PageNotFound from "./components/PageNotFound/PageNotFound";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/appointment" element={<Appointment />} />
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
