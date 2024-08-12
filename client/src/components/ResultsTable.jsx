const ResultsTable = ({ results }) => {
  return (
    <div className="grid gap-4">
      <h2 className="text-2xl font-bold">Resultados</h2>
      <div className="overflow-auto border rounded-lg">
        <table className="w-full border-collapse">
          <thead>
            <tr className="border-b">
              <th className="p-2">Lista</th>
              <th className="p-2">Votos</th>
              <th className="p-2">Escaños</th>
            </tr>
          </thead>
          <tbody>
            {results.length > 0 ? (
              results.map((item, i) => (
                <tr key={i} className="border-b">
                  <td className="p-2">{item.name}</td>
                  <td className="p-2">{item.votes}</td>
                  <td className="p-2">{item.seats}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="3" className="p-2 text-center text-gray-500">
                  No hay resultados para mostrar
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ResultsTable;
