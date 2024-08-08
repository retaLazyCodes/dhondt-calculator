import React from 'react';
import VotesItem from './VotesItem';

function ListVotes({ 
  lists, 
  handleListsChange, 
  removeList,
  disableVotesInput = false 
}) {
  return (
    <div className="grid gap-2">
      {lists.map((list, i) => (
        <VotesItem
          key={i}
          list={list}
          index={i}
          handleListsChange={handleListsChange}
          removeList={removeList}
          disableVotesInput={disableVotesInput}
        />
      ))}
    </div>
  );
}

export default ListVotes;
