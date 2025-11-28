import Header from "../components/Header";
import Footer from "../components/Footer";
import { Link } from "react-router-dom";

function LoginPage() {
  return (
    <div className="bg-gradient-to-t from-teal-950  to bg-teal-800 h-screen w-screen bg-cover bg-center ">
      <Header />
      <p
        className="flex h-135 w-250 ml-67 mt-14 bg-gradient-to-r from-white/19 to-white/19 rounded-lg rounded-b-md font-bold text-white
      "
      >
        <div>
          {" "}
          <p className="font-bold text-5xl text-white flex pl-30 pt-17">
            Olá, Bem vindo!
          </p>
          <p className="font-bold text-white pl-40 text-xl pt-9 ">
            Ainda não possui um conta?
          </p>
          <div>
            <Link
              to="/register"
              className="flex items-center justify-center h-10 w-80 ml-32 mt-19 bg-transparent text-white font-bold py-3 px-8 border-3 border-white/5 hover:bg-white/89 hover:text-black transition duration-300 rounded-lg rounded-b-md"
            >
              Cadastrar-se
            </Link>
            <p className="text-sm flex pt-38 pl-28">
              Ajudando você a transformar necessidades em soluções.
            </p>
          </div>
        </div>
      </p>
      <Footer />
    </div>
  );
}

export default LoginPage;
