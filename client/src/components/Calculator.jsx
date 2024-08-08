import React, { useState } from 'react';
import SeatCountInput from './SeatCountInput';
import ListVotes from './ListVotes';
import VotesCountInput from './VotesCountInput';
import ResultsTable from './ResultsTable';
import HistoryTable from './HistoryTable';

function Calculator() {
  const [seats, setSeats] = useState(1);
  const [initialVotes, setInitialVotes] = useState(0);
  const [lists, setLists] = useState([]);
  const [history, setHistory] = useState([]);
  const [results, setResults] = useState([]);

  const handleSeatsChange = (e) => {
    setSeats(parseInt(e.target.value));
  };

  const handleInitialVotesChange = (e) => {
    setInitialVotes(parseInt(e.target.value));
  };

  const handleListsChange = (index, name, votes) => {
    const newLists = [...lists];
    newLists[index] = { name, votes: parseInt(votes) };
    setLists(newLists);
  };

  const addList = () => {
    setLists([...lists, { name: `Lista #${lists.length + 1}`, votes: initialVotes }]);
  };

  const removeList = (index) => {
    const newLists = [...lists];
    newLists.splice(index, 1);
    setLists(newLists);
  };

  const calculateSeats = () => {
    const quotients = lists.map((list) => ({ ...list, seats: 0 }));
    for (let i = 0; i < seats; i++) {
      const maxQuotient = quotients.reduce(
        (max, q) => (q.votes / (q.seats + 1) > max.votes / (max.seats + 1) ? q : max),
        quotients[0]
      );
      maxQuotient.seats++;
    }
    const result = quotients.sort((a, b) => b.seats - a.seats);
    setHistory([...history, { seats, lists, result }]);
    setResults(result);
  };

  const clearHistory = () => {
    setHistory([]);
  };


  return (
    <div className="flex flex-col gap-8 p-8 max-w-4xl mx-auto">
      <div className="grid gap-4">
        <h1 className="text-3xl font-bold">Calculadora de distribución de escaños D'Hondt</h1>
        <p className="text-muted-foreground">
          Introduzca el número de escaños a repartir, luego agregue la cantidad de listas que desee, cada una con sus respectivos votos, a continuación presione el botón "Calcular escaños" para ver la distribución de los escaños.
        </p>
      </div>
      <div className="grid gap-4">
        <SeatCountInput value={seats} onChange={handleSeatsChange} />
        <VotesCountInput value={initialVotes} onChange={handleInitialVotesChange} />
        <div className="grid gap-2">
          <button onClick={addList} className="p-2 border rounded-md">
            Nueva Lista
          </button>
          <ListVotes
            lists={lists}
            handleListsChange={handleListsChange}
            removeList={removeList}
            disableVotesInput={false}
          />
        </div>
      </div>
      <div className="grid gap-4">
        <div className="flex justify-between">
          <button onClick={calculateSeats} className="p-2 border rounded-md">
            Calcular escaños
          </button>
          <div className="flex gap-2">
            <button onClick={clearHistory} className="p-2 border rounded-md">
              Limpiar Historial
            </button>
          </div>
        </div>
        <ResultsTable results={results} />
      </div>
      <HistoryTable history={history} />
    </div>
  );
}

export default Calculator;
