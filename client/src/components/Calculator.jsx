import { useState } from 'react';
import SeatCountInput from './SeatCountInput';
import ListVotes from './ListVotes';
import ResultsTable from './ResultsTable';
import HistoryTable from './HistoryTable';
import NewListButton from './NewListButton';
import CalculateButton from './CalculateButton';
import ClearHistoryButton from './ClearHistoryButton';

function Calculator() {
  const [seats, setSeats] = useState(1 | NaN);
  const [lists, setLists] = useState([]);
  const [history, setHistory] = useState([]);
  const [results, setResults] = useState([]);

  const handleSeatsChange = (e) => {
    if (e.target.value) {
      setSeats(parseInt(e.target.value));
    } else {
      setSeats(NaN);
    }
  };

  const handleListsChange = (index, name, votes) => {
    const newLists = [...lists];
    newLists[index] = { name, votes: parseInt(votes) };
    setLists(newLists);
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

    const result = [...quotients].sort((a, b) => b.seats - a.seats);

    setHistory([...history, { seats, lists: result, result }]);
    setResults(result);
  };

  const clearHistory = () => {
    setHistory([]);
  };

  return (
    <div className="flex flex-col gap-8 p-8 max-w-4xl mx-auto">
      <div className="grid gap-4">
        <h1 className="text-3xl font-bold">Calculadora de distribución de escaños D'Hondt</h1>
      </div>
      <div className="grid gap-4">
        <SeatCountInput 
          value={seats} 
          onChange={handleSeatsChange} 
        />
        <div className="grid gap-2">
          <NewListButton
            setLists={setLists} 
            lists={lists} 
          />
          <ListVotes
            lists={lists}
            handleListsChange={handleListsChange}
            removeList={removeList}
          />
        </div>
      </div>
      <div className="grid gap-4">
        <div className="flex justify-between">
          <CalculateButton onClick={calculateSeats} lists={lists} />
          <ClearHistoryButton onClick={clearHistory} history={history} />
        </div>
        <ResultsTable results={results} />
      </div>
      <HistoryTable history={history} />
    </div>
  );
}

export default Calculator;
