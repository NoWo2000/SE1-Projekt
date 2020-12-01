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
                time: "date and time",
                affectedSystems: [],
                suspectedAttackType: "Suspected Attack Type",
                probability: 0,
                automaticReaction: [],
                checklist: []
            }],
            alarmArrayReversed: []
        };

        subscribeToEvent((err, EventData) => {
            EventData.time = EventData.time * 1000;
            this.setState({ alarmArray: [...this.state.alarmArray, EventData] });
        });

        this.generateAlarm = this.generateAlarm.bind(this);
    }

    componentDidMount() {
        let start = (+ new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate()) / 1000);
        fetch(`/api/alerts?start=${start}`)
            .then(result => result.json())
            .then(
                (result) => {
                    result.map(alarm => {
                        alarm.time = alarm.time * 1000;
                        return null;
                    })
                    this.setState({
                        alarmArray: this.state.alarmArray.concat(result)
                    });
                },
                (error) => {
                    console.log(error);
                }
            )
    }

    generateAlarm() {
        this.setState({ alarmArray: [...this.state.alarmArray, generateRandomAlarm()] });
    }

    render() {

        let reversedArray = [...this.state.alarmArray];
        reversedArray.reverse();

        return (
            <Container fluid>
                {/* Header */}
                <Row>
                    <h1 class="mx-auto mt-2 pb-4 pt-1" onClick={this.generateAlarm}>GUI - Alarm Detection Software</h1>
                </Row>
                {/* Main Content */}
                <Row>
                    {/* Alarm List */}
                    <Col md={6}>
                        <Accordion defaultActiveKey={reversedArray[0]}>
                            {reversedArray.map(alarm => {
                                if (alarm.probability >= 75) {
                                    return <Alarm data={alarm}></Alarm>;
                                } else {
                                    return null;
                                }
                            })}
                        </Accordion>
                    </Col>
                    {/* 24h-Course */}
                    <Col>
                        <Chart data={this.state.alarmArray}></Chart>
                    </Col>
                </Row>
            </Container >
        );
    }
}

export default App;