import { Link } from "react-router-dom";
import Footer from "../components/Footer";
import Header from "../components/Header";
function RegisterPage() {
  return (
    <div>
      <div className="bg-gradient-to-t from-teal-950  to bg-teal-800 h-screen w-screen bg-cover bg-center ">
        <Header />
        <p
          className="flex h-135 w-250 ml-67 mt-14 bg-gradient-to-r from-white/19 to-white/19 rounded-lg rounded-b-md font-bold text-white
      "
        >
          <div>
            {" "}
            <p className="font-bold text-5xl text-white flex pl-60 pt-10">
              Cadastre-se por aqui!
            </p>
            <div></div>
          </div>
        </p>
        <Footer />
      </div>
    </div>
  );
}

export default RegisterPage;
