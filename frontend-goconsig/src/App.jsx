import Header from "./components/Header";
import Footer from "./components/Footer";

function App() {

  return (
    <div className="w-screen h-screen bg-white flex justify-center p-6">
      <div className="w-[500px]">
      <Header />
      <h1 className=" mt-10 text-3xl text-blue-900 font-bold text-center ">Bem-vindo ao GoConsig!</h1>
      <Footer />
      </div>
    </div>
  )
}

export default App;