import React from 'react';
import PropTypes from 'prop-types';

function Nav(props:any) {
  const loggedOutNav = (
    <ul>
      <li onClick={() => props.displayForm('login')}>login</li>
      <li onClick={() => props.displayForm('signup')}>signup</li>
    </ul>
  );

  const loggedInNav = (
    <ul>
      <li onClick={props.handleLogout}>logout</li>
    </ul>
  );
  return <div>{props.logged_in ? loggedInNav : loggedOutNav}</div>;
}

export default Nav;

Nav.propTypes = {
  logged_in: PropTypes.bool.isRequired,
  displayForm: PropTypes.func.isRequired,
  handleLogout: PropTypes.func.isRequired
};