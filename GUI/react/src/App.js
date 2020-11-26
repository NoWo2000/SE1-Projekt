import React from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Alarm from './Alarm.js';
import subscribeToEvent from './api';

class App extends React.Component {

    constructor(props) {
        super(props);

        subscribeToEvent((err, EventData) => this.setState({
            EventData
        }));
    }
    state = {
        EventData: {}

    }

    render() {
        return (
            <Container fluid>
                {/* Header */}
                <Row>
                    <h1>Alarm Dashboard</h1>
                </Row>
                {/* Main Content */}
                <Row>
                    {/* Alarm List */}
                    <Col>
                        <Accordion defaultActiveKey="0">
                            <Alarm card_head="test"></Alarm>
                        </Accordion>
                    </Col>
                    {/* 24h-Course */}
                    <Col>24h-Course</Col>
                </Row>
            </Container>);
    }
}

export default App;