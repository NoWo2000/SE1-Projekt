import React from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Alarm from './Alarm.js';
import Chart from './Chart.js';
import { subscribeToEvent } from '../api.js';
import { generateRandomAlarm } from '../generateAlarm.js';


class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            alarmArray: [{
                id: "ID",
                date: "date and time",
                affectedSystems: [],
                suspectedAttackType: "Suspected Attack Type",
                probability: 0,
                automaticReaction: [],
                checklist: []
            }
            ]
        };

        subscribeToEvent((err, EventData) => {
            this.setState({ alarmArray: [...this.state.alarmArray, EventData] })
        });

        this.generateAlarm = this.generateAlarm.bind(this);
    }

    generateAlarm() {
        this.setState({ alarmArray: [...this.state.alarmArray, generateRandomAlarm()] });
        this.forceUpdate();
    }

    render() {
        return (
            <Container fluid>
                {/* Header */}
                <Row>
                    <h1 class="mx-auto mt-2" onClick={this.generateAlarm}>GUI - Alarm Detection Software</h1>
                </Row>
                {/* Main Content */}
                <Row>
                    {/* Alarm List */}
                    <Col md={6}>
                        <Accordion defaultActiveKey={this.state.alarmArray[0]}>
                            {this.state.alarmArray.map(alarm => {
                                return <Alarm data={alarm}></Alarm>
                            })}
                        </Accordion>
                    </Col>
                    <Col id="chart">
                        {/* 24h-Course */}
                        <Chart data={this.state.alarmArray}></Chart>
                    </Col>
                </Row>
            </Container >
        );
    }
}

export default App;