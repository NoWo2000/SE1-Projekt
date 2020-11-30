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
            alarmArrayReversed:[]
        };

        subscribeToEvent((err, EventData) => {
            this.setState({ alarmArray: [...this.state.alarmArray, EventData] });
        });

        this.generateAlarm = this.generateAlarm.bind(this);
    }

    componentDidMount() {
        let start = (+ new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate())/1000);
        fetch(`http://gns3.p-fruck.de/api/alerts?start=${start}`)
            .then(result => result.json())
            .then(
                (result) => {
                    result.map(alarm => {
                        alarm.time = alarm.time * 1000;
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
        let a = [...this.state.alarmArray, generateRandomAlarm()]
        this.setState({ alarmArray: a });
    }

    render() {
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
                        <Accordion defaultActiveKey={this.state.alarmArray[0]}>
                            {this.state.alarmArray.map(alarm => {
                                if (alarm.probability >= 75) {
                                    return <Alarm data={alarm}></Alarm>
                                } else {
                                    return ""
                                }
                            })}
                        </Accordion>
                    </Col>
                    <Col>
                        {/* 24h-Course */}
                        <Chart data={this.state.alarmArray}></Chart>
                    </Col>
                </Row>
            </Container >
        );
    }
}

export default App;