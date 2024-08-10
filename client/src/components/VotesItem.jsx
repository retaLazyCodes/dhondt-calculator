import { useState } from 'react';

function VotesItem({ 
  list, 
  index, 
  handleListsChange, 
  removeList, 
  disableVotesInput = false 
}) {
  const [isVotesInputDisabled, setIsVotesInputDisabled] = useState(disableVotesInput);

  const toggleVotesInput = () => {
    setIsVotesInputDisabled(!isVotesInputDisabled);
  };

  return (
    <div className="flex gap-2 items-center">
      <input
        type="text"
        placeholder="List Name"
        value={list.name}
        onChange={(e) => handleListsChange(index, e.target.value, list.votes)}
        className="flex-1 p-2 border rounded-md"
        disabled
      />
      <input
        type="number"
        min="0"
        value={list.votes}
        onChange={(e) => handleListsChange(index, list.name, e.target.value)}
        className="flex-1 p-2 border rounded-md"
        disabled={isVotesInputDisabled}
      />
      {isVotesInputDisabled ? (
        <button
          onClick={toggleVotesInput}
          className="p-2 text-blue-500 hover:bg-blue-500/10 rounded-md"
        >
          ✏️
        </button>
      ) : (
        <button
          onClick={toggleVotesInput}
          className="p-2 text-green-500 hover:bg-green-500/10 rounded-md"
        >
          ✅
        </button>
      )}
      <button
        onClick={() => removeList(index)}
        className="p-2 text-red-500 hover:bg-red-500/10 rounded-md"
      >
        🗑️
      </button>
    </div>
  );
}

export default VotesItem;
