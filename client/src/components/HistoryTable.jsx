const HistoryTable = ({ history }) => {
  if (history.length === 0) return null;
  
  return (
    <div className="grid gap-4">
      <h2 className="text-2xl font-bold">Historial de cálculos</h2>
      <div className="overflow-auto border rounded-lg">
        <table className="w-full border-collapse">
          <thead>
            <tr className="border-b">
              <th className="p-2">Lista</th>
              <th className="p-2">Votos</th>
              <th className="p-2">Escaños</th>
              <th className="p-2">Resultado</th>
            </tr>
          </thead>
          <tbody>
            {history.map((item, i) => (
              <tr key={i} className="border-b">
                <td className="p-2">
                  {item.lists.map((l, j) => (
                    <div key={j}>{l.name}</div>
                  ))}
                </td>
                <td className="p-2">
                  {item.lists.map((l, j) => (
                    <div key={j}>{l.votes}</div>
                  ))}
                </td>
                <td className="p-2">{item.seats}</td>
                <td className="p-2">
                  {item.result.map((r, j) => (
                    <div key={j}>{r.seats}</div>
                  ))}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default HistoryTable;
