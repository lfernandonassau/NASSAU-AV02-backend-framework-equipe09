function Header() {
  return (
    //Header (topo do site), aq pelo menos tentou a organização

    <header className="h-15 flex justify-between">
      <div>
        <h1 className="font-bold text-4xl ml-8 text-white pt-2">
          <a href="/">GoConsig</a>
        </h1>
      </div>
      <div className="hidden md:flex space-x-6 ml pt-4 px-10">
        <a
          href="/"
          className="text-gray-300 hover:text-white transition duration-300"
        >
          Home
        </a>
        <a
          href="#sobre"
          className="text-gray-300 hover:text-white transition duration-300"
        >
          Sobre
        </a>
        <a
          href="#servicos"
          className="text-gray-300 hover:text-white transition duration-300"
        >
          Serviços
        </a>
        <a
          href="#contato"
          className="text-gray-300 hover:text-white transition duration-300"
        >
          Contato
        </a>
      </div>
    </header>
  );
}

export default Header;
