import Header from "./components/Header";
import Footer from "./components/Footer";
import { Link } from "react-router-dom";

function App() {
  return (
    //plano de fundo,  (sim, as divs tão bem suspeitas, mas dá um desconto fiz isso aq de madrugada)
    <div className="bg-[url('../src/assets/Finace.jpg')]  h-screen w-screen bg-cover bg-center">
      <Header />

      <div>
        <h1 className="flex items-center ml-10  mt-50 text-7xl text-white font-bold ">
          Bem-vindo ao GoConsig!
        </h1>
      </div>
      <div>
        <h2 className="flex items-center ml-20  mt-2 text-2xl text-white font-bold">
          o melhor site de simulação de empréstimos do mercado
        </h2>
      </div>
      <div>
        <Link //Botão de Login, talvez me complique no futuro com isso
          to="/login"
          className="flex items-center justify-center h-16 w-80 ml-32 mt-19 bg-transparent text-white font-bold py-3 px-8 border-3 border-white/5 hover:bg-white/89 hover:text-black transition duration-300 rounded-lg rounded-b-md"
        >
          Entrar agora!
        </Link>
      </div>
      <Footer />
    </div>
  );
}

export default App;
